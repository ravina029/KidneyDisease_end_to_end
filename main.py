from kidneyDiseaseClassifier import logger
from kidneyDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from kidneyDiseaseClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from kidneyDiseaseClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline 
from kidneyDiseaseClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

STAGE_NAME="Data ingestion stage"

try:
    logger.info(f">>>>>>> stage{STAGE_NAME} started <<<<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n x=============x")
except Exception as e:
         logger.exception(e)
         raise e


 
STAGE_NAME="Prepare Base Model"

try:
        logger.info(f"************************")
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj=PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx===============x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME="Training"
try:
        logger.info(f"************************")
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        model_trainer=ModelTrainingPipeline()
        model_trainer.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx===============x")
except Exception as e:
        logger.exception(e)
        raise e 




STAGE_NAME = "Evaluation stage"

try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        
except Exception as e:
        logger.exception(e)
        raise e