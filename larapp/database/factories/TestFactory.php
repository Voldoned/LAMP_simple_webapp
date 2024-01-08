<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;
use App\Models\Test;
/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\=Tests>
 */
class TestFactory extends Factory
{
    protected $model = Test::class;
    
    
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        return [
            'quetion' => 'Когда был создан PHP?',
            'answer1' => 'В 1994 году.',
            'answer2' => 'В 1986 году.',
            'answer3' => 'В 1990 году.',
            'answer4' => 'В 2000 году.',
            'answer_true' => 'В 1994 году.',
        ];
    }
}
