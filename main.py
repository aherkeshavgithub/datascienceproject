from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline                                                      
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline 
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline

logger.info("Welcome to our cutome logging data science project")


STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} stated>>>>>>>>>>>")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>>>> Stage {STAGE_NAME} completed >>>>><<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Validation Stage"

try:   
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} stated>>>>>>>>>>>")
    data_ingestion=DataValidationTrainingPipeline()
    data_ingestion.initiate_data_validation()
    logger.info(f">>>>>>>> Stage {STAGE_NAME} completed >>>>><<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Transformation Stage"

try:
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} stated>>>>>>>>>>>")
    data_ingestion=DataTransformationTrainingPipeline()
    data_ingestion.initiate_data_transformation()
    logger.info(f">>>>>>>> Stage {STAGE_NAME} completed >>>>><<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} stated>>>>>>>>>>>")
    data_ingestion=ModelTrainerTrainingPipeline()
    data_ingestion.initiate_model_training()
    logger.info(f">>>>>>>> Stage {STAGE_NAME} completed >>>>><<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e