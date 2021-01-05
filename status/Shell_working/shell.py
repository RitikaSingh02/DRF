>> > all = User.objects.filter(username="perfect.entry").values()
>> > all
# <QuerySet [{'id': 18, 'password': 'KIET123', 'last_login': datetime.datetime(2020, 11, 15, 23, 35, 19, 273824, tzinfo= < UTC > ), 'is_superuser': False, 'username': 'perfect.entry', 'first_name': '', 'last_name': '', 'email': 'adam@gmail.com', 'is_staff': False, 'is_active': True, 'date_joined': datetime.datetime(2020, 11, 14, 12, 15, 24, 699387, tzinfo= < UTC > )}] >
>> > data = StatusSerializer({'user': 18})
>> > print(repr(data))
StatusSerializer({'user': 18}):
    id = IntegerField(label='ID', read_only=True)
    content = CharField(allow_blank=True, allow_null=True, required=False, style={
                        'base_template': 'textarea.html'})
    image = ImageField(allow_null=True, max_length=100, required=False)
    email = EmailField(allow_null=True, max_length=254, required=False, validators=[< UniqueValidator(queryset=Status.objects.all()) > ])
    timestamp = DateTimeField(read_only=True)
    user = PrimaryKeyRelatedField(
        allow_null=True, queryset=User.objects.all(), required=False)


# since we paased a python instance so we did not put many=True for passing Queries we put many=True
>> > s = StatusSerializer({'user': 18})
>> > s.is_valid()
# Traceback(most recent call last):
#   File "<console>", line 1, in <module >
#   File "/home/ritika/.local/lib/python3.9/site-packages/rest_framework/serializers.py", line 213, in is_valid
#     assert hasattr(self, 'initial_data'), (
# AssertionError: Cannot call `.is_valid()` as no `data=` keyword argument was passed when instantiating the serializer instance.
>> > s = StatusSerializer(data={'user': 18})
>> > s.is_valid()
True
