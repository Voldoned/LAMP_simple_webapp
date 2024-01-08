<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Http\Requests\Tests\StoreRequest;
use App\Models\Test;
use Illuminate\Http\Request;

class StoreController extends Controller
{
    public function __invoke(StoreRequest $request) {
        $validated = $request->validated();
        $new_test = [
            'quetion' => $validated['quetion'], 
            'answer1' => $validated['answer1'], 
            'answer2' => $validated['answer2'], 
            'answer3' => $validated['answer3'], 
            'answer4' => $validated['answer4'], 
            'answer_true' => $validated[$validated['answer_true']], 
        ]; 
        
        $created_test = Test::create($new_test);
    	return response()->json($created_test);
    }
}
