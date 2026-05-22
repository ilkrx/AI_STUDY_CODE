import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# 查看设备，运行在CPU或者cuda
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("模型会运行在：", device)

# 实例化一个因果语言模型，并且放在设备上：CPU或者cuda
model = AutoModelForCausalLM.from_pretrained("./models/Qwen/Qwen2___5-0___5B-Instruct")
# 实例化一个分词器
tokenizer = AutoTokenizer.from_pretrained("./models/Qwen/Qwen2___5-0___5B-Instruct")

# 设置prompt
prompt = "你是谁？"

# 组建message
messages = [
    {"role": "system", "content": "You are a helpful assiatant."},
    {"role": "user", "content": prompt},
    # {"role": "assistant", "content": "{"}
]

# 使用分词器将对话转换成适用于模型输入的格式，并添加生成提示
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
print(text)
model_inputs = tokenizer([text], return_tensors="pt")
print(model_inputs)

# 预测新的token序列，最大生成512个token
generated_ids = model.generate(
    model_inputs.input_ids,
    max_new_tokens=512
)

# 截取生成tokens部分
generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)