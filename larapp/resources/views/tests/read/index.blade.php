<!DOCTYPE html>
<html>
    <head>
        <title>Тест на знание PHP</title>
    </head>
    <body>
        <h1>
            Тест на знание PHP
        </h1>
        <form method="post" action="{{ route('test.post') }}">
            @csrf

            {{-- Проверка на наличие ошибок --}}
            @if($errors->any())
                <div>
                    <ul>
                        @foreach($errors->all() as $message)
                            <li>{{ $message }}</li>
                        @endforeach
                    </ul>
                </div>
            @endif
            
            <div>
                {{-- Цикл вывода тестовых вопросов --}}
                @foreach($quetions as $quetion)
                    <p>
                        {{ $quetion->quetion }}<br>

                        {{-- Цикл вывода вариантов ответа --}}
                        @foreach([$quetion->answer1, $quetion->answer2, $quetion->answer3, $quetion->answer4] as $answer)
                            <input type="radio" name="q{{ $quetion->id }}" value="{{ $answer }}"> {{ $answer }}<br>
                        @endforeach
                    </p>
                @endforeach
                <input type="submit" value="Проверить ответы">
            </div>
        </form>
    </body>
</html>