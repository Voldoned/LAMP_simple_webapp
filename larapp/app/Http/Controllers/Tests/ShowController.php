<?php

namespace App\Http\Controllers\Tests;

use App\Http\Controllers\Controller;
use App\Models\Test;
use Exception;
use Illuminate\Http\Request;

class ShowController extends Controller
{
    public function __invoke() {
        // При отправке клиентом полностью заполненной формы, срабатывает
        // блок try. Если же отправлена клиентом пустая или частично
        // заполненная форма, то срабатывает блок catch.
        try {
            if ($_SERVER["REQUEST_METHOD"] == "POST") {
                $quetions = Test::all();

                // Подсчёт количества правильных ответов
                $score = 0;
                foreach ($quetions as $quetion) {
                    $qi = "q{$quetion->id}";
                    $q_true = $quetion->answer_true;
                    if ($_POST[$qi] == $q_true) { $score++; }
                }

                return view('tests.read.store', compact('score'));
            }
        } catch (Exception) {
            return view('tests.read.error');
        }
    }
}
