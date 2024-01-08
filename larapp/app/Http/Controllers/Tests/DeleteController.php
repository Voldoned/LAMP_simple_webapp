<?php

namespace App\Http\Controllers\Tests;

use App\Http\Controllers\Controller;
use App\Models\Test;
use Illuminate\Http\Request;

class DeleteController extends Controller
{
    public function __invoke() {
        $quetions = Test::all();
    	return view('tests.delete.index', compact('quetions'));
    }
}
