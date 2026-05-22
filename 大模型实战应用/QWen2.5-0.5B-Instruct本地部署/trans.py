from transformers import AutoTokenizer

# 实例化一个分词器
tokenizer = AutoTokenizer.from_pretrained("./models/Qwen/Qwen2___5-0___5B-Instruct")

model_inputs = tokenizer(["你好"], return_tensors="pt")

print("model_inputs:", model_inputs)

# token_ids = model_inputs["input_ids"].squeeze().tolist()
token_ids = [105043]
response = tokenizer.decode(token_ids=token_ids)
print("response:", response, "--------")