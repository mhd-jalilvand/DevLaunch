from utils.software import Software
window_width = 500
window_height = 600
active_icon = '\u25B6'  # Play icon
stopped_icon = '\u25A0'  # Stop rectangle
active_color = 'green'
stopped_color = 'red'
software_list = [
    Software("Nginx", "apt-get install nginx", "nginx -v 2>&1", "apt-get upgrade nginx"),
    Software("Apache", "apt-get install apache", "apache -v 2>&1", "apt-get upgrade apache"),
    Software("MySQL", "apt-get install mysql", "mysql -V", "apt-get upgrade mysql"),
    Software("composer", "apt-get install composer", "composer -V", "apt-get upgrade composer")
]