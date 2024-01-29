from transformers import GPT2Model, GPT2Config, AutoTokenizer

model_name = "gpt2"  # or specify the model name you need
model = GPT2Model.from_pretrained(model_name)
config = GPT2Config.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Save the model and tokenizer to the desired directory
model.save_pretrained("D:/privateGPT/models/ggml-gpt4all-j-v1.3-groovy")
tokenizer.save_pretrained("D:/privateGPT/models/ggml-gpt4all-j-v1.3-groovy")
