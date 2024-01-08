<?php

namespace App\Http\Controllers\Tests;

use App\Http\Controllers\Controller;
use App\Http\Requests\Tests\StoreRequest;
use App\Models\Test;
use Illuminate\Http\Request;

class StoreController extends Controller
{
    public function __invoke(StoreRequest $request) {
        $validated = $request->validated();

        // В данном случае в $validated'answer_true'] 
        // хранится КЛЮЧ массива $validated
        // с правильным ответом (например, 
        // в $validated у ключа 'answer_true' => 'answer2'). 
        // Поэтому, чтобы получить ЗНАЧЕНИЕ правильного ответа, 
        // мы результат $validated['answer_true'] используем 
        // как ключ асоциативного массива $validated.

        $new_test = [
            'quetion' => $validated['quetion'], 
            'answer1' => $validated['answer1'], 
            'answer2' => $validated['answer2'], 
            'answer3' => $validated['answer3'], 
            'answer4' => $validated['answer4'], 
            'answer_true' => $validated[$validated['answer_true']], 
        ]; 
        
        Test::create($validated);

        return redirect()->route('test.index');
    }
}
