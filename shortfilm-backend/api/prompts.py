def break_prompt_into_scenes(main_prompt):
    return [
        {'scene_prompt': f'{main_prompt} - scene 1', 'script': 'This is script 1'},
        {'scene_prompt': f'{main_prompt} - scene 2', 'script': 'This is script 2'},
    ]
