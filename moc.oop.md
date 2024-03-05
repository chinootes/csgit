---
id: tv91pcfe2tgsqlzk67vgbrp
title: Object Oriented Design and Programming
desc: ''
updated: 1708452976545
created: 1708179490422
---

## Entities/Components

- [[programming.paradigm.oo.components.class]]
- [[programming.paradigm.oo.components.object]]
- [[programming.paradigm.oo.components.class.friend]]
- [[programming.paradigm.oo.components.members]]
- [[programming.paradigm.oo.components.covariant return type]]

## Four Pillars + one secret basement of OOP

- [[programming.paradigm.oo.pillars.polymorphism]]
  - [[programming.paradigm.oo.pillars.polymorphism.overloading]]
  - [[programming.paradigm.oo.pillars.polymorphism.overriding]]: [[programming.paradigm.oo.components.covariant return type]]
- [[programming.paradigm.oo.pillars.inheritance]]
  - [[programming.paradigm.oo.pillars.inheritance.types.single]]
  - [[programming.paradigm.oo.pillars.inheritance.types.multilevel]]
  - [[programming.paradigm.oo.pillars.inheritance.types.multiple]]
  - [[programming.paradigm.oo.pillars.inheritance.types.hierarchical]]
  - [[programming.paradigm.oo.pillars.inheritance.types.hybrid]]
- [[programming.paradigm.oo.pillars.encapsulation]]
- [[programming.paradigm.oo.pillars.abstraction]] \ [[programming.paradigm.oo.components.types.abstract]]
  - [[programming.paradigm.oo.components.interface]] \ [[programming.paradigm.oo.components.types.abstract.class]] 
  - [[design.oo.use cases for.abstract class]]
    - [[design.oo.use cases for.abstract class.providing flexible behavior for related classes]]
    - [[design.oo.use cases for.abstract class.helper]]
    - [[design.oo.use cases for.abstract class.stepping stone]]
- [[programming.paradigm.oo.pillars.association]]
  - [[programming.paradigm.oo.pillars.association.aggregation]]
    - [[programming.paradigm.oo.pillars.association.aggregation.composition]]
      - [[design.oo.principles.composition over inheritance]]
        - [[programming.paradigm.oo.pillars.inheritance.purpose]] vs [[programming.paradigm.oo.pillars.inheritance.disadvantages]]
        - [[programming.paradigm.oo.pillars.association.aggregation.composition.benefits]] vs [[programming.paradigm.oo.pillars.association.aggregation.composition.disadvantages]]

## OOP Features

- [[programming.paradigm.oo.features.binding.static]]
- [[programming.paradigm.oo.features.binding.dynamic]]
- [[programming.paradigm.oo.pillars.polymorphism.runtime]]
- [[programming.paradigm.oo.features.shadowing]]
- [[type theory.substitutability]]
- [[type theory.variance]]

## Types of members/classes

- [[programming.paradigm.oo.components.types.static]]
  - [[programming.paradigm.oo.components.types.static.variable]]
: [[programming.paradigm.oo.components.types.static.variable.serialization]]
  - [[programming.paradigm.oo.components.types.static.method]]: [[programming.paradigm.oo.components.types.static.method.accessing instance variables]]
  - [[programming.paradigm.oo.components.types.static.access using objects]]
  - [[programming.paradigm.oo.components.types.static.overriding]]
  - [[programming.paradigm.oo.components.types.static.overriding.fail]]
- [[programming.paradigm.oo.components.types.final]]
- [[programming.paradigm.oo.components.types.abstract]]: [[programming.paradigm.oo.components.types.abstract.class]]

## Accessing/referring objects

- [[programming.paradigm.oo.context.object.self-reference]]
- [[programming.paradigm.oo.context.object.super]]

## Playing with Objects

- [[programming.paradigm.oo.components.object.cloning]]
- [[type theory.casting.object]]: [[type theory.casting.object.upcasting]] \ [[type theory.casting.object.downcasting]]
- [[programming.paradigm.oo.components.object.serialization]]
- [[programming.paradigm.oo.components.object.deserialization]]

## Object Oriented Design

- [[design.oo.application with no constraints]]
- [[design.oo.use cases for.interface]]
- [[design.oo.use cases for.abstract class]]
  - [[design.oo.use cases for.abstract class.providing flexible behavior for related classes]]
  - [[design.oo.use cases for.abstract class.helper]]
  - But it is okay to use [[design.oo.use cases for.abstract class.stepping stone]]

### [[design.oo.patterns]]

- [[design.oo.patterns.gof]]
  - [[design.oo.patterns.gof.creational]]s
    - [[design.oo.patterns.gof.creational.singleton]]
    - [[design.oo.patterns.gof.creational.factory]]
    - [[design.oo.patterns.gof.creational.builder]]
    - [[design.oo.patterns.gof.creational.dependency injection]] and [[design.oo.principles.ioc]]
      - [[Dependency]]
      - [[design.oo.patterns.gof.creational.dependency injection.constructor]]
      - [[design.oo.patterns.gof.creational.dependency injection.setter]]
      - [[design.oo.patterns.gof.creational.dependency injection.parameter]]
      - [[design.oo.patterns.gof.creational.dependency injection.backdoor]]
  - [[design.oo.patterns.gof.structural]]
    -[[design.oo.patterns.gof.structural.marker]]
  - [[design.oo.patterns.gof.behavioural]]
    - [[design.oo.patterns.gof.behavioural.dao]]
    - [[design.oo.patterns.gof.behavioural.strategy]]
    - 