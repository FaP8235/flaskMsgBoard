from flask import flash, redirect, url_for, render_template
from flaskMsgBoard import app, db
from flaskMsgBoard.models import Message
from flaskMsgBoard.forms import MsgBoardForm


@app.route('/', methods=['GET', 'POST'])
def index():
    # 初始化MsgBoardForm表单对象
    form = MsgBoardForm()
    # 验证表单是否正确提交
    if form.validate_on_submit():
        # 获取表单数据
        name = form.name.data
        body = form.body.data
        # 初始化Message数据表对象
        message = Message(body=body, name=name)
        # 数据库事务添加与提交
        db.session.add(message)
        db.session.commit()
        # 提交完成后发送提示
        flash('您的信息已经发送！')
        return redirect(url_for('index'))
    # 加载所有记录
    # 查询数据库
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    # 将查询到的数据加载到模板页面
    return render_template('index.html', form=form, messages=messages)