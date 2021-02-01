from parlai.scripts.train_model import TrainModel

TrainModel.main(
    model_file='from_scratch_model1/model',
    task='jsonfile', jsonfile_datapath='output.jsonl',
    batchsize=16,
    validation_every_n_secs=5 * 60,
    model='seq2seq',
    attention='dot',
    lookuptable='all',
    truncate=64,
)
