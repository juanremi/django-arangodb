# Pablo Carreira - 15/10/16
import django
import pytest

from arangodb_driver.models.aql.query import AQLQuerySet

django.setup()

from sample_app.models import Person, Group


@pytest.mark.skip(reason="not implemented yet")
def test_insert():
    joao = Person(name='Foo', age=35)
    joao.save()
    group1 = Group(name='Rock Band')
    group1.save()

    joao.groups.add(group1)

    print("Group:")
    j_groups = joao.groups.all()
    for item in j_groups:
        print(item.name)




@pytest.mark.skip(reason="not implemented yet")
def test_get():
    bacon = Person(name='Bacon')
    bacon.save()
    pk = int(bacon.pk)
    assert isinstance(pk, int)
    bacon = None
    bacon = Person.objects.get(pk=str(pk))
    assert isinstance(bacon, Person)
    assert bacon.name == 'Bacon'

@pytest.mark.skip(reason="not implemented yet")
def test_filter_simple():
    # TODO: Move to test setup.
    # Person(name='Eggs', age=30).save()
    # Person(name='Eggs', age=31).save()
    # Person(name='Eggs', age=32).save()
    queryset_a = Person.objects.filter(name='Eggs')
    assert isinstance(queryset_a, AQLQuerySet)
    assert len(queryset_a) >= 3

@pytest.mark.skip(reason="not implemented yet")
def test_filter_kwargs():
    # TODO: Move to test setup.
    # ages = [30, 31, 31]
    # for age in ages:
    #     a = Person(name='Eggs', age=age)
    #     a.save()
    queryset_b = Person.objects.filter(name='Eggs', age=31)
    assert isinstance(queryset_b, AQLQuerySet)
    assert len(queryset_b) >= 2
    for item in queryset_b:
        print(item.name)

@pytest.mark.skip(reason="not implemented yet")
def test_filter_chaining():
    queryset_b = Person.objects.filter(name='Eggs').filter(age=31)
    assert isinstance(queryset_b, AQLQuerySet)
    assert len(queryset_b) >= 2
    for item in queryset_b:
        print(item.name)

@pytest.mark.skip(reason="not implemented yet")
def test_delete_model():
    queryset = Person.objects.filter(name='Eggs', age=31)
    len_a = len(queryset)
    queryset[0].delete()
    # Refetch to make sure that its updated.
    queryset = Person.objects.filter(name='Eggs', age=31)
    len_b = len(queryset)
    print(len_a)
    print(len_b)
    assert len_a > len_b


@pytest.mark.skip(reason="not implemented yet")
def test_delete_queryset():
    queryset = Person.objects.filter(name='Eggs', age=31)
    len_a = len(queryset)
    queryset.delete()
    assert len_a == 0


@pytest.mark.skip(reason="not implemented yet")
def test_filter_operators():
    raise NotImplementedError


@pytest.mark.skip(reason="not implemented yet")
def test_bulk_delete():
    pass


if __name__ == '__main__':
    test_insert()