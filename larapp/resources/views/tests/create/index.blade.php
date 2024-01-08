<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>
            Форма для создания тестового вопроса
        </title>
    </head>
    <body>
        <h1>
            Форма для создания тестового вопроса
        </h1>
        <form method="post" action="{{ route('create_test.post') }}">
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
                <label for="quetion">
                    Вопрос:
                </label>
                <input type="text" id="quetion" name="quetion"><br><br>
                
                {{-- Вывод полей для заполнения вариантов ответа на тестовый вопрос --}}
                @for ($i = 1; $i < 5; $i++)
                    <label for="answer{{$i}}">
                        Вариант ответа {{$i}}:
                    </label>
                    <input type="text" id="answer{{$i}}" name="answer{{$i}}"><br><br>
                @endfor

                <label for="answer_true">
                    Правильный ответ:
                </label>
                <select id="answer_true" name="answer_true">

                    {{-- Вывод кнопок для выбора правильного ответа --}}
                    @for ($i = 1; $i < 5; $i++)
                        <option value="answer{{$i}}">
                            Вариант ответа {{$i}}
                        </option>
                    @endfor
                    
                </select><br><br>
                <input type="submit" value="Создать вопрос">
            </div>
        </form>
    </body>
</html>