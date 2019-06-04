MalformattedRequestError = Exception('the request is malformatted, i.e. missing content')
DeviceNotFoundError = Exception('a device couldn\'t be found')
UserNotFoundError = Exception('user couldn\'t be found (incorrect username/password)')
IncorrectCredentialsError = Exception('credentials are incorrect')
UnauthorizedError = Exception('package name or api key is incorrect')