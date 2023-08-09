from Exercise_1.app import db, app, Owner, Car

with app.app_context():
    db.drop_all() # Delete this line once I've started putting data in my database
    db.create_all()
    # testUser = Users(first_name)

    testuser = Owner(first_name="earl", last_name="gray")
    db.session.add(testuser)
    db.session.commit()

    testcar = Car(num_plate = "bf7 h8w", ownerbr=testuser)
    db.session.add(testcar)
    db.session.commit()
    testcar2 = Car(num_plate = "bf6 h8w", ownerbr=testuser)
    db.session.add(testcar2)
    db.session.commit()
    testcar3 = Car(num_plate = "bf5 h8w", ownerbr=testuser)
    db.session.add(testcar3)
    db.session.commit()

    print(testcar.ownerbr.first_name)
    print(testuser.cars[1].num_plate)

    testitem = Car.query.filter_by(num_plate="bf5 h8w").first()
    print(testitem.id, testitem.num_plate)

    # car_to_change = Car.query.get(1)
    # print(car_to_change)

    # car_to_delete = Car.query.filter_by(id=2).first()
    # db.session.delete(car_to_delete)
    # db.session.commit()