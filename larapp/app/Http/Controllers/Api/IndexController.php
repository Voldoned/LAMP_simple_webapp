<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Test;
use Illuminate\Http\Request;

class IndexController extends Controller
{
    public function __invoke() {
        $tests = Test::all();
    	return response()->json($tests);
    }
}
