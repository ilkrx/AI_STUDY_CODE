from modelscope.hub.snapshot_download import snapshot_download


# Qwen/Qwen2.5-0.5B-Instruct为魔搭社区上的路径，models为本地路劲
llm_model_dir = snapshot_download('Qwen/Qwen2.5-0.5B-Instruct',cache_dir='models')