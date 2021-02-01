from parlai.scripts.train_model import TrainModel

TrainModel.main(
    model_file='from_scratch_model/model',
    task='jsonfile', jsonfile_datapath='output.jsonl',
    batchsize=16, fp16=True, fp16_impl='mem_efficient',
    model='seq2seq',
    embedding_type='fasttext',
    lr=1e-5, optimizer='adam',
    warmup_updates=100,
    validation_metric='ppl',
    validation_every_n_secs=5 * 60,
    skip_generation=True,
    dynamic_batching='full',
    truncate=64,
)
