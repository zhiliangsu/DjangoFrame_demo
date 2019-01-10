def my_middleware(get_response):
    print('init 被调用')

    def middleware(request):
        print('before request 被调用')
        response = get_response(request)
        print('after response 被调用')
        return response

    return middleware


def my_middleware2(get_response):
    print('init2 被调用')

    def middleware(request):
        print('before request 2 被调用')
        response = get_response(request)
        print('after response 2 被调用')
        return response

    return middleware

# 中间件执行原理是: 请求时自上而下的,响应是自下而上的
