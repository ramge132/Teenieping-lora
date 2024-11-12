import os
from dotenv import load_dotenv
import replicate

load_dotenv()

replicate_api_token = os.getenv("REPLICATE_API_TOKEN")

os.environ["REPLICATE_API_TOKEN"] = replicate_api_token

training = replicate.trainings.create(
   destination="ramge132/teenieping-lora",
   version="ostris/flux-dev-lora-trainer:e440909d3512c31646ee2e0c7d6f6f4923224863a6a10c494606e79fb5844497",
   input={
      "steps": 6000,
      "lora_rank": 16,
      "optimizer": "adamw8bit",
      "batch_size": 1,
      "hf_repo_id": "Ramge/teenieping-lora",
      "resolution": "512,768,1024",
      "autocaption": True,
      "input_images": open("data/teenieping_png.zip", "rb"),
      "trigger_word": "TEENIEPINGLORA",
      "learning_rate": 0.0004,
      "wandb_project": "flux_train_replicate",
      "autocaption_prefix": "a photo of teenieping",
      "wandb_save_interval": 100,
      "caption_dropout_rate": 0.05,
      "cache_latents_to_disk": False,
      "wandb_sample_interval": 100
   },
)