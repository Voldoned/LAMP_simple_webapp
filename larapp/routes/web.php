<?php

use App\Http\Controllers\Tests;

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Route::get('/test', Tests\IndexController::class)->name('test.index');
Route::post('/test/post', Tests\ShowController::class)->name('test.post');

Route::get('/test/create', Tests\CreateController::class)->name('create_test.index');
Route::post('/test/create/post', Tests\StoreController::class)->name('create_test.post');

Route::get('/test/delete', Tests\DeleteController::class)->name('delete_test.index');
Route::post('/test/delete/post', Tests\DropController::class)->name('delete_test.post');