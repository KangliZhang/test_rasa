# test_rasa

Rasa 版本 3.3.0 ，Rasa SDK 版本 3.3.0

rasa shell 启动命令之后  输入 init 激活 Form

待验证两点：
1、在 action 里面如果把 extract_is_someone 方法注释掉，Form 表单不会循环 ask slot ，尽管 extract_is_someone 这个方法里面什么都没做，只是 return  {"is_someone": is_someone}

2、action_ask_is_someone 这个 action 里面，requested_slot 的值是滞后的，执行完action_ask_is_someone 这个 action 之后，requested_slot 的值才会被更新

以上是我验证的结论
