from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_evaluation import ModelEvaluation

STAGE_NAME= "Model Evaluation Stage"

class ModelEvalautionTrainingPipeline:
    def __init__(self):
        pass
    def initiate_model_evaluation_training_pipeline(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()