from parlai.scripts.train_model import TrainModel

TrainModel.main(
    # similar to before
    task='empathetic_dialogues',
    model='transformer/generator',
    model_file='from_pretrained/model',

    init_model='zoo:tutorial_transformer_generator/model',

    n_heads=16, n_layers=8, n_positions=512, text_truncate=512,
    label_truncate=128, ffn_size=2048, embedding_size=512,
    activation='gelu', variant='xlm',
    dict_lower=True, dict_tokenizer='bpe',
    dict_file='zoo:tutorial_transformer_generator/model.dict',
    learn_positional_embeddings=True,

    lr=1e-5, optimizer='adam',
    warmup_updates=100,
    validation_metric='ppl',  # perplexity
    max_train_time=600, validation_every_n_epochs=0.25,

    batchsize=12, fp16=True, fp16_impl='mem_efficient',

    skip_generation=True,

    dynamic_batching='full',
)
