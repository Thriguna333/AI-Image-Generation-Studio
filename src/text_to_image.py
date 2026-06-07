def generate_image(
    prompt,
    negative_prompt,
    cfg_scale,
    inference_steps
):

    return f"""
Prompt: {prompt}

Negative Prompt: {negative_prompt}

CFG Scale: {cfg_scale}

Inference Steps: {inference_steps}

Image generation request received.
"""