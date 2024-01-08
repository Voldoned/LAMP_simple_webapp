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
            Вы создали следующий тестовый вопрос:
        </h1>
        <div>
            <p>
                {{ $new_test['quetion'] }}
            </p>
        </div>
        <div>
            <table>
                <tr>
                    <td>a.</td>
                    <td>{{ $new_test['answer1'] }}</td>
                </tr>
                <tr>
                    <td>b.</td>
                    <td>{{ $new_test['answer2'] }}</td>
                </tr>
                <tr>
                    <td>c.</td>
                    <td>{{ $new_test['answer3'] }}</td>
                </tr>
                <tr>
                    <td>d.</td>
                    <td>{{ $new_test['answer4'] }}</td>
                </tr>
                <tr>
                    <td>true</td>
                    <td>{{ $new_test['answer_true']}}</td>
                </tr>
            </table>
        </div>
    </body>
</html>