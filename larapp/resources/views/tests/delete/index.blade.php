<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Вопрос добавлен в тест!</title>
    </head>
    <body>
        <h1>
            Выберите ID вопроса, который необходимо удалить, из приведенного ниже списка
        </h1>
        <div>
            <form method="post" action="{{ route('delete_test.post') }}">
                @csrf
                <label for="id_quetion">
                    ID тестового вопроса:
                </label>
                <input type="text" id="id_quetion" name="id_quetion"><br><br>
                <input type="submit" value="Удалить вопрос">
            </form>
        </div>
        <div>
            {{--Вывод всех тестовых вопросов с соответствующими им ID в базе данных--}}
            @foreach ($quetions as $quetion)
                <div>
                    <table>
                        <tr>
                            <th>ID = {{ $quetion->id }}</th>
                            <th>{{ $quetion->quetion }}</th>
                        </tr> 
                        <tr>
                            <td>a.</td>
                            <td>{{ $quetion->answer1 }}</td>
                        </tr>
                        <tr>
                            <td>b.</td>
                            <td>{{ $quetion->answer2 }}</td>
                        </tr>
                        <tr>
                            <td>c.</td>
                            <td>{{ $quetion->answer3 }}</td>
                        </tr>
                        <tr>
                            <td>d.</td>
                            <td>{{ $quetion->answer4 }}</td>
                        </tr>
                        <tr>
                            <td>true</td>
                            <td>{{ $quetion->answer_true }}</td>
                        </tr>
                    </table>
                </div>
            @endforeach
        </div>
    </body>
</html>