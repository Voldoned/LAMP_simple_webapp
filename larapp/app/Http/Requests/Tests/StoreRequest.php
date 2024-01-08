<?php

namespace App\Http\Requests\Tests;

use Illuminate\Foundation\Http\FormRequest;

class StoreRequest extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     */
    public function authorize(): bool
    {
        return true;
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, \Illuminate\Contracts\Validation\ValidationRule|array|string>
     */
    public function rules(): array
    {
        return [
            'quetion' => ['required', 'string'],
            'answer1' => ['required', 'string'],
            'answer2' => ['required', 'string'],
            'answer3' => ['required', 'string'],
            'answer4' => ['required', 'string'],
            'answer_true' => ['required', 'string']
        ];
    }
}
