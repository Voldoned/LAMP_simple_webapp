<?php

namespace App\Http\Controllers\Tests;

use App\Http\Controllers\Controller;
use App\Models\Test;
use Illuminate\Http\Request;

class IndexController extends Controller
{
    public function __invoke() {
        $quetions = Test::all();
    	return view('tests.read.index', compact('quetions'));
    }
}
