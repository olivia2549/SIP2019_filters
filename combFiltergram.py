import combFilters

def main():
    puppyImage = combFilters.load_img("puppy.jpg")
    obamicon_puppyImage = combFilters.obamicon(puppyImage)
    yellowPurple_puppyImage = combFilters.yellow_purple(puppyImage)
    alien_puppyImage = combFilters.alien(puppyImage)
    monochromatic_puppyImage = combFilters.monochromatic(puppyImage)
    hello_puppyImage = combFilters.hello(puppyImage)
    owneon_puppyImage = combFilters.owneon(puppyImage)
    thanoss_puppyImage = combFilters.thanoss(puppyImage)
    flaggy_puppyImage = combFilters.flaggy(puppyImage)
    combFilters.save_img(obamicon_puppyImage, "obamiPuppy.jpg")
    combFilters.save_img(yellowPurple_puppyImage, "ypPuppy.jpg")
    combFilters.save_img(alien_puppyImage, "alienPuppy.jpg")
    combFilters.save_img(monochromatic_puppyImage, "monoPuppy.jpg")
    combFilters.save_img(hello_puppyImage, "helloPuppy.jpg")
    combFilters.save_img(owneon_puppyImage, "owneonPuppy.jpg")
    combFilters.save_img(thanoss_puppyImage, "thanossPuppy.jpg")
    combFilters.save_img(flaggy_puppyImage, "flaggyPuppy.jpg")

if __name__ == "__main__":
    main()
