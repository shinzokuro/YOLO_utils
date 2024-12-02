import argparse
from pathlib import Path


def create_val_config(weights_path, data_path, project_path, name):
    # Creating an argparse.Namespace manually
    opt = argparse.Namespace(
        data=Path(data_path),
        weights=Path(weights_path),
        batch_size=32,
        imgsz=640,
        conf_thres=0.001,
        iou_thres=0.6,
        max_det=300,
        task="val",
        device="",
        workers=8,
        single_cls=True,
        augment=False,
        verbose=False,
        save_txt=False,
        save_hybrid=False,
        save_conf=False,
        save_json=False,
        project=Path(project_path),
        name=name,
        exist_ok=False,
        half=False,
        dnn=False,
    )
    return opt


def create_train_config(
    train_yaml,
    dataset_dir,
    model_dir,
):
    opt = argparse.Namespace(
        weights=train_yaml["weights"],
        cfg=train_yaml["cfg"],
        data=Path(dataset_dir / train_yaml["data"]),
        hyp=Path(dataset_dir / train_yaml["hyp"]),
        epochs=train_yaml["epochs"],
        batch_size=train_yaml["batch_size"],
        imgsz=train_yaml["imgsz"],
        rect=train_yaml["rect"],
        resume=train_yaml["resume"],
        nosave=train_yaml["nosave"],
        noval=train_yaml["noval"],
        noautoanchor=train_yaml["noautoanchor"],
        noplots=train_yaml["noplots"],
        evolve=train_yaml["evolve"],
        evolve_population=train_yaml["evolve_population"],
        resume_evolve=train_yaml["resume_evolve"],
        bucket=train_yaml["bucket"],
        cache=train_yaml["cache"],
        image_weights=train_yaml["image_weights"],
        device=train_yaml["device"],
        multi_scale=train_yaml["multi_scale"],
        single_cls=train_yaml["single_cls"],
        optimizer=train_yaml["optimizer"],
        sync_bn=train_yaml["sync_bn"],
        workers=train_yaml["workers"],
        project=Path(model_dir / train_yaml["project"]),
        name=train_yaml["name"],
        exist_ok=train_yaml["exist_ok"],
        quad=train_yaml["quad"],
        cos_lr=train_yaml["cos_lr"],
        label_smoothing=train_yaml["label_smoothing"],
        patience=train_yaml["patience"],
        freeze=train_yaml["freeze"],
        save_period=train_yaml["save_period"],
        seed=train_yaml["seed"],
        local_rank=train_yaml["local_rank"],
        entity=train_yaml["entity"],
        upload_dataset=train_yaml["upload_dataset"],
        bbox_interval=train_yaml["bbox_interval"],
        artifact_alias=train_yaml["artifact_alias"],
        ndjson_console=train_yaml["ndjson_console"],
        ndjson_file=train_yaml["ndjson_file"],
    )
    return opt
