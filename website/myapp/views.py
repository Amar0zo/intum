from django.shortcuts import render
from myapp.robot import Robot

def index(request):
    if request.method == 'POST':
        robot_ip = request.POST.get('robot_ip')
        robot = Robot()
        if robot.connect(robot_ip):
            return HttpResponse('Robot connected successfully!')
        else:
            return HttpResponse('Failed to connect to the robot!')
    return render(request, 'index.html')

    if request.method == 'POST':
        robot.send_command('brake release')

   # robot.disconnect()

    return render(request, 'index.html', {'connected': robot.connected})
