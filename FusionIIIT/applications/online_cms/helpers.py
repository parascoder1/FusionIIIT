from datetime import datetime


def semester(roll):
    month = datetime.now().month
    sem = 0
    if month >= 8 and month <= 12:
        sem = 1
    semester = (datetime.now().year-int(roll))*2+sem
    return semester


def create_thumbnail(course, row, name, ext, attach_str, thumb_time, thumb_size):
    filepath = settings.MEDIA_ROOT + '/online_cms/' + course.course_id + '/vid/' + name + ext
#    video_name = row.video_name[:-4]
    filename = settings.MEDIA_ROOT + '/online_cms/' + course.course_id + '/vid/'
    filename = filename + name.replace(' ', '-') + '-' + attach_str + '.png'
    process = 'ffmpeg -y -i ' + filepath + ' -vframes ' + str(1) + ' -an -s '
    process = process + thumb_size + ' -ss ' + str(thumb_time) + ' ' + filename
    subprocess.call(process, shell=True)


def find_courses(user):
    extrainfo = ExtraInfo.objects.get(user=user)
    if extrainfo.user_type == 'student':
        student = Student.objects.get(id=extrainfo)
        roll = student.id.id[:4]
        course = Course.objects.filter(course_id=course_code, sem=semester(roll))
        return course
