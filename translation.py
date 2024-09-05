#%% packages
from transformers import pipeline



#%% translation
pipe = pipeline("translation_en_to_pt", model="danhsf/m2m100_418M-finetuned-kde4-en-to-pt_BR")
pipe("The capital of France is Paris.")
# %%
