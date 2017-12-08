今天看到一个比较好的github学习系列技术贴，让我下决心正式好好使用github。

首先贴出原文链接：

		【1】github的历史和用途：http://stormzhang.com/github/2016/05/25/learn-github-from-zero1/

		【2】注册及新建github仓库：http://stormzhang.com/github/2016/05/26/learn-github-from-zero2/

		【3】git安装及本地创建SSH Key：http://blog.csdn.net/chengyuqiang/article/details/54178683

		【4】git常用方法：http://stormzhang.com/github/2016/05/30/learn-github-from-zero3/

着重强调：

【1】GitHub 基本概念：

		Repository

		译为仓库，即你创建的项目，你想在 GitHub 上开源一个项目，那就必须要新建一个 Repository。
		在个人主页右上角有个“+”标志，点击之后选择“New repository”可以新建仓库

		Issue

		译为问题，举个例子，就是你开源了一个项目，别人发现你的项目中有bug，或者哪些地方做的不够好，
		他就可以给你提个Issue，然后你看到了这些问题就可以去逐个修复，修复ok了就可以一个个的 Close 掉。

		Star

		这个好理解，就是给项目点赞

		Fork

		译为分叉。如果你看到比较中意的别人的项目，然后你可以fork，这时你的 GitHub 主页上就多了一个项目，
		你可以在别人的工作基础上进行任意改进，但是丝毫不会影响原作者项目的代码与结构。

		Pull Request

		发起请求，这个其实是基于 Fork 的。比如你在别人基础进行改进并希望将自己的改动合并到原项目，这时
		可以发起Pull Request，如果原作者认同你的改动并接受你的PR，你的改进原有项目就会拥有了。

		Watch

		译为观察，如果你 Watch 了某个项目，那么以后只要这个项目有任何更新，你都会第一时间收到关于这个项目的通知提醒。

		Gist

		有些时候你没有项目可以开源，只是单纯的想分享一些代码片段，那这个时候 Gist 就派上用场了！

【2】如何把别人的项目和代码复制到本地并Pull Request给原作者

		在你想复制的文件夹下右键Git Bash

		接着输入以下代码：

		git clone ‘这里应该是仓库链接地址’

		//添加全部

		git add -A

		//提交全部

		git commit -m 'first commit'

		//提交到服务器

		git push

		现在回到github主页看到有Pull Request更新，然后点击Pull Request以及creat Pull Request

		最后就是等待原作者同意了。
		
【3】改动自己建立的仓库并上传

		1、git add -A

		2、git commit -m 'first commit'

		3、git push