import torch
from diffusers import StableDiffusionPipeline

# Detect device
if torch.backends.mps.is_available():
    device = "mps"
    print("Using MPS")
elif torch.cuda.is_available():
    device = "cuda"
    print("Using CUDA")
else:
    device = "cpu"
    print("Running on CPU (Slower).")

# Load Stable Diffusion with optimized settings for low memory
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float32
)
pipe.to(device)

pipe.enable_attention_slicing()


def generate_image(prompt):
    """
    Generate an image from a text prompt using Stable Diffusion.
    Optimized for MPS to avoid memory errors.
    """
    with torch.no_grad():
        image = pipe(
            prompt,
            height=384,
            width=384,
            num_inference_steps=20
        ).images[0]

    image.show()
    image.save("generated_image.png")


if __name__ == "__main__":
    prompt = input("Enter a text prompt: ")
    generate_image(prompt)
