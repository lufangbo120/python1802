# 主入口
(
 celery -A TopSpeedData_Worker.celery_app worker  -Q TSD_Tasks_Main  -n Queue_TSD_Taisks_Main@%d --logfile=logout\TSD_Default.log &
 celery -A TopSpeedData_Worker.celery_app worker  -Q TSD_Default  -n Queue_TSD_Default@%d --logfile=logout\TSD_Default.log &
 celery -A TopSpeedData_Worker.celery_app worker  -Q TSD_Periodictask -n Queue_TTSD_Periodictask@%d --logfile=logout\TSD_Periodictask.log &
)