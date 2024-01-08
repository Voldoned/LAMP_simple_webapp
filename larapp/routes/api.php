<?php

use App\Http\Controllers\Api\DropController;
use App\Http\Controllers\Api\IndexController;
use App\Http\Controllers\Api\StoreController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
|
*/

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});

Route::get('/tests', IndexController::class)->withoutMiddleware("throttle:api");
Route::post('/test/create/post', StoreController::class)->withoutMiddleware("throttle:api");
Route::post('/test/delete/post', DropController::class)->withoutMiddleware("throttle:api");
