def state(traits,log):
    for trait in traits:
        if str.lower(trait[-3:]) != 'png':
            log.logger.warning(f"{trait}不為png格式可能會發生合成錯誤!(請保持asset資料夾從都為png格式)")
