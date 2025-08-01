from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_validation  import DataValidation
from src.datascience import logger

STAGE_NAME="Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_validation(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.validation_all_columnns()

if __name__=="__main__":
    try:
        logger.info(f">>>>>>>>>> Stage {STAGE_NAME} stated>>>>>>>>>>>")
        obj=DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>>>> Stage {STAGE_NAME} completed >>>>><<<<<<<\n\nx===========x")
    except Exception as e:
        logger.exception(e)
        raise e
    