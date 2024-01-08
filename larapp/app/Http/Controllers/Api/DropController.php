<?php

namespace App\Http\Controllers\Api;

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

            // Проверяем наличие записи с id, равной введенному значению
            if ($quetion->exists()) {
                $quetion->delete();
                return response()->json($quetion);
            } else {
                return response()->json([
                    'error' => 'No exist quetion with this ID'
                ]);
            }
        } catch (Exception) {
            return response()->json([
                'error' => 'Empty value in label ID or bad form-data'
            ]);
        }
    }
}
