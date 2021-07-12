help=input('您好，欢迎来到古灵阁，请问您需要帮助吗？需要or不需要？')


if help=='需要':
    choice=int(input('请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询'))

    if choice ==1:
        print('请去存取款窗口。')

    elif choice==2:
        print('金加隆和人民币的兑换率为1:51.3，既1金加隆=51.3人民币')
        money=input('请问您需要兑换多少金加隆呢？')
        print('好的，我知道了，您需要兑换'+money+'金加隆。')
        print('那么，您需要付给我'+str(float(money)*51.3)+'人民币。')


    else:
        print('请去咨询窗口。')


else:
    print('好的，再见。')