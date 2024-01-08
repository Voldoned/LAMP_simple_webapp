<?php

namespace App\Http\Controllers\Tests;

use App\Http\Controllers\Controller;
use App\Models\Test;
use Exception;
use Illuminate\Http\Request;

class DropController extends Controller
{
    public function __invoke() {
        // При отправке клиентом полностью заполненной формы, срабатывает
        // блок try. Если же отправлена клиентом пустая или частично
        // заполненная форма, то срабатывает блок catch.
        try {
            $quetion_id = $_POST["id_quetion"];
            $quetion = Test::where('id', $quetion_id);
            if ($quetion->exists()) {
                $quetion->delete();
                return view('tests.delete.store', compact('quetion_id'));
            } else {
                return view('tests.delete.error');
            }
        } catch (Exception) {
            return view('tests.read.error');
        }
    }
}
