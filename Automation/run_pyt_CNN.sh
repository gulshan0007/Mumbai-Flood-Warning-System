cd /home/subimal/Documents/HDFC_Web/Automation/
/home/subimal/anaconda3/bin/python /home/subimal/Documents/HDFC_Web/Automation/GFS_1day_download-3hour.py
/home/subimal/anaconda3/bin/python /home/subimal/Documents/HDFC_Web/Automation/boxplot17.30-Copy1.py
rsync -avhu /home/subimal/Documents/HDFC_Web/Automation/* /var/www/html/ULL/Automation/
rm /var/www/html/ULL/Automation/Automate.ipynb
rm /var/www/html/ULL/Automation/boxplot17.30.ipynb
rm /var/www/html/ULL/Automation/boxplot17.30-Copy1.ipynb
rm /var/www/html/ULL/Automation/boxplot17.30-Copy1.py
rm /var/www/html/ULL/Automation/GFS_1day_download-3hour.ipynb
rm /var/www/html/ULL/Automation/GFS_1day_download-3hour.py

