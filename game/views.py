from django.shortcuts import render
from django.views import View
from .forms import GameForm, GameCreateForm
from .models import Game, Player, PlayerGameInfo


class GameView(View):
    def get(self, request):
        context = {}

        if request.GET.get('q') == 'create':
            context['create_form'] = GameCreateForm()
            return render(request, 'create.html', context=context)

        elif request.GET.get('q') == 'play':
            context['game_form'] = GameCreateForm()
            return render(request, 'play.html', context=context)

        player, created = Player.objects.get_or_create(id=request.session.get('player_id'))
        game = Game.objects.get(owner=player) if not created else None
        context['game'] = game

        return render(request, 'home.html', context=context)

    def post(self, request):
        context = {}

        player, created = Player.objects.get_or_create(id=request.session.get('player_id'))
        request.session['player_id'] = player.id

        if request.GET.get('q') == 'create':
            form = GameCreateForm(request.POST)
            context['create_form'] = form
            if form.is_valid():
                game = form.save(commit=False)
                game.owner = player
                game.save()
            return render(request, 'create.html', context=context)

        elif request.GET.get('q') == 'play':
            form = GameCreateForm(request.POST)
            context['game_form'] = form
            if form.is_valid():
                game = Game.objects.get(id=request.GET.get('game'))
                number = form.cleaned_data['number']
                game.players.add(player)

                th = game.playergameinfo_set.get(player=player)
                th.attempts += 1
                th.save()

                if number == game.number:
                    context['message'] = 'Вы угадали загаданное число!'
                    context.pop('game_form')
                    game.solved = True
                else:
                    pass

                if number > game.number:
                    context['message'] = 'Введенное число больше угадываемого.'
                if number < game.number:
                    context['message'] = 'Введенное число меньше угадываемого.'

            return render(request, 'play.html', context=context)

        return render(request, 'home.html', context=context)
