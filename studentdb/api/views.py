from rest_framework import status, response, views
from foundation.models import StudentDB

class AddAPIView(views.APIView):
    def post(self, request):
        student_first_name = request.data.get('fname', None)
        student_last_name = request.data.get('lname', None)
        student_mark = request.data.get('mark', None)
        student_email = request.data.get('email', None)

        if student_first_name == None and student_last_name == None and student_mark == None and student_email == None:
            return response.Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={
                  'message': 'Missing field.',
                  })
        else:
            first_name = student_first_name
            last_name = student_last_name
            mark = float(student_mark)
            email = student_email
            memory =  StudentDB.objects.create(fname = first_name, lname = last_name, mark = student_mark, email = student_email)
            memory.save()
            print(first_name+" "+last_name+" "+str(mark) +" " + email)
            return response.Response(
            status=status.HTTP_200_OK,
            data={
                 'message': 'Student Registered  Successfully!',
                 })


class StudentListAPIView(views.APIView):
    def get(self,request):
        student_list = []
        student_data = StudentDB.objects.all().order_by('id').values('fname','lname','mark')
        for student_datum in student_data:
            student_list.append(student_datum['fname'])
        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'Student List': str(student_list),
                }
                )
class StudentDetailAPIView(views.APIView):
    def get(self,request,id):
        try:
            student_detail = StudentDB.objects.get(pk=id)
            return response.Response(
                status=status.HTTP_200_OK,
                data={
                'Student First Name': student_detail.fname,
                'Student Last Name': student_detail.lname,
                'Student Mark': student_detail.mark,
                'Student Email': student_detail.email,
                })

        except Exception as e:
            return response.Response(
                status=status.HTTP_404_NOT_FOUND,
                data={
                'message': 'No details found',
                     })
class StudentUpdateAPIView(views.APIView):
    def put(self, request, id):
        first_name = request.data.get('fname', None)
        last_name = request.data.get('lname', None)
        mark = request.data.get('mark', None)
        email = request.data.get('email', None)
        if first_name == None or last_name == None or mark == None or email == None:
            return response.Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={
            'message': 'Missing field',
                 })
        else:
            try:
                memory = StudentDB.objects.get(id = id)
                memory.fname = first_name
                memory.lname = last_name
                memory.mark = mark
                memory.email = email
                memory.save()
                return response.Response(
                status=status.HTTP_200_OK,
                data={
                'Student Updation Status': 'Student Detail Successfully Updated',
                'Student First Name': memory.fname,
                'Student Last Name': memory.lname,
                'Student Mark': memory.mark,
                'Student Email': memory.email,
                     })

            except Exception as e:
                return response.Response(
                status=status.HTTP_404_NOT_FOUND,
                data={
                'message': 'Updation failed due to '+str(e),
                     })


class ClearStudentRecordsAPIView(views.APIView):
    def post(self,request, id):
        def delete(self,request,id):
        memory = StudentDB.objects.get(id=id)

        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'message': "Memory has been cleared successfully!",
            }
        )
