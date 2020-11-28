from unittest.mock import MagicMock

from src.services.logging_service import LoggingService


def test_logger_is_only_ever_built_once_per_instance():
    logger = LoggingService('test')
    logger._build_logger = MagicMock()

    mock_logger = logger._build_logger.return_value

    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.exception('exception')

    mock_logger.info.assert_called_with('info')
    mock_logger.warning.assert_called_with('warning')
    mock_logger.error.assert_called_with('error')
    mock_logger.exception.assert_called_with('exception')

    assert 1 == logger._build_logger.call_count
